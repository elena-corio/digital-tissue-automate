from domain.model.elements import Model


def filter_model(model, filter_fn):
    return Model(
        columns=[column for column in model.columns if filter_fn(column)],
        cores=[core for core in model.cores if filter_fn(core)],
        facades=[facade for facade in model.facades if filter_fn(facade)],
        open_spaces=[open_space for open_space in model.open_spaces if filter_fn(open_space)],
        slabs=[slab for slab in model.slabs if filter_fn(slab)],
        units=[unit for unit in model.units if filter_fn(unit)],
        volumes=[volume for volume in model.volumes if filter_fn(volume)],
    )