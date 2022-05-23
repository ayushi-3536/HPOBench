import logging
import pytest

logging.basicConfig(level=logging.DEBUG)


def test_adult_benchmark():
    from hpobench.benchmarks.mo.adult_benchmark import AdultBenchmark

    # Check Seeding
    benchmark = AdultBenchmark(rng=0)
    cs = benchmark.get_configuration_space(seed=0)
    cfg_1 = cs.sample_configuration()

    cs = benchmark.get_configuration_space(seed=0)
    cfg_2 = cs.sample_configuration()

    assert cfg_1 == cfg_2

    print("cfg1",cfg_1)
    print("cfg2",cfg_2)

    test_config = {
        'alpha': 0.00046568046379195655, 'beta_1': 0.14382335124614148, 'beta_2': 0.0010007892350251595,
        'fc_layer_0': 4, 'fc_layer_1': 2, 'fc_layer_2': 2, 'fc_layer_3': 3,'n_fc_layers': 4,'learning_rate_init': 0.0005343227125594117,
        'tol': 0.0004134759007834719
    }

    result_1 = benchmark.objective_function(test_config, rng=1, fidelity={'budget': 3})
    result_2 = benchmark.objective_function(test_config, rng=1, fidelity={'budget': 3})
    print("r1",result_1)
    print("r2",result_2)

    assert result_1['info']['train_accuracy'] == pytest.approx(0.76145, rel=0.001)
    assert result_1['info']['train_accuracy'] == result_2['info']['train_accuracy']